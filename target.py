class Target:
    def __init__(self, tgt_id, tgt_type):
        self.tgt_id = tgt_id
        self.tgt_type = tgt_type

    def get_tgt_id(self):
        return self.tgt_id
    
    def get_tgt_type(self):
        return self.get_tgt_type