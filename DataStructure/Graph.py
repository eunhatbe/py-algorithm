class Graph:
    def __init__(self, vertex_num = None) -> None:
        # 인접리스트
        self.adj_list = []
        self.vtx_num = 0

        # 정점이 있으면 True 없으면 False
        self.vtx_arr = []
        
        if vertex_num: # 정점 개수
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]

            # 연결리스트 대신 동적 배열 사용
            self.adj_list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        return False

    def add_vertex(self):
        for i in range(len(self.vtx_arr))
            
