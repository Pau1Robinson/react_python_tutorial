from repository import Repository
from repository.mongo import MongoRepository
from schema import PFRMSchema

class Service(object):
    def __init__(self, user_id, repo_client=Repository(adapter=MongoRepository)):
        self.repo_client = repo_client
        self.user_id = user_id

        if not user_id:
            raise Exception('user id not provided')

    def find_PFRM(self, repo_id):
        PFRM = self.repo_client.find({'user_id':self.user_id, 'repo_id': repo_id})
        return self.dump(PFRM)

    def create_PFRM_for(self, githubRepo):
        self.repo_client.create(self.prepare_PFRM(githubRepo))
        return self.dump(githubRepo.data)

    def update_PFRM_with(self, repo_id, githubRepo):
        records_affected = self.repo_client.update({'user_id': self.user_id, 'repo_id':repo_id}, self.prepare_PFRM(githubRepo))
        return records_affected > 0

    def delete_PFRM_for(self, repo_id):
        records_affected = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
        return records_affected > 0

    def dump(self, data):
        return PFRMSchema(exclude=['_id'].dump(data)).data

    def prepare_PFRM(self, githubRepo):
        data = githubRepo.data
        data['user_id'] = self.user_id
        return data