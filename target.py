from posicao import Posicao

class Target:
    def __init__(self, tgt_id:int, tgt_type:str, tgt_posicao:Posicao):
        self.tgt_id = tgt_id
        self.tgt_type = tgt_type
        self.tgt_posicao = tgt_posicao

    def get_tgt_id(self):
        return self.tgt_id
    
    def get_tgt_type(self):
        return self.get_tgt_type