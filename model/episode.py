import time
from json import dumps, loads
from services.database import MyDatabase

class EpisodeModel:
    database_service: MyDatabase = None
    def __init__(self, title, sinopsis, season, id=None) -> None:
        if id:
            self.id = id
        else:
            highest_id = int(max(self.seek_existing_ids())) if self.seek_existing_ids() else 0
            self.id = highest_id + 1
        self.title = title
        self.sinopsis = sinopsis
        self.season = season

    @classmethod
    def add_episode(cls, episode):
        cls.database_service.create_episode(episode)     

    @classmethod
    def find_episode(cls, episode_id):
        found_episode = None
        result = cls.database_service.find_movie(episode_id)
        if result:
            found_episode = EpisodeModel(result[1], result[2], result[3], result[0])
        return found_episode   
    
    @classmethod
    def remove_episode(cls, episode):
        cls.database_service.delete_episode(episode)
    
    @classmethod
    def list_to_dict(cls):
        result = cls.database_service.list_episodes()
        episode_list = []
        for episode in result:
            episode_list.append(EpisodeModel(episode[1], episode[2], episode[3], episode[0]))
        return loads(dumps(episode_list, default=EpisodeModel.to_dict))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "sinopsis": self.sinopsis,
            "season": self.season
        }

    @classmethod
    def seek_existing_ids(cls):
        result = cls.database_service.list_episodes()
        id_list = []
        for episode in result:
            id_list.append(episode[0])
        return sorted(id_list)
