# pip install baidu-aip
from aip import AipFace
import base64

class BaiDuFace:
    # 注册应用有的
    def __init__(self, APP_ID='62643893', API_KEY='hfAwQUE1fwyCjXG01ZCHbaSG',
                 SECRET_KEY='qgxJneAt0ovmGA2rLrdq99GEFs1apjte'):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.client = AipFace(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    # 注册人脸
    def add_user(self):
        # 把图片转成base64
        image =base64.b64encode(open('./dlrbb.png','rb').read()).decode('utf-8')
        imageType = "BASE64"
        groupId = "100"
        userId = "dilireba"
        """ 调用人脸注册 """
        # client.addUser(image, imageType, groupId, userId);

        """ 如果有可选参数 """
        options = {}
        options["user_info"] = "这是迪丽热巴"
        options["quality_control"] = "NORMAL"
        options["liveness_control"] = "LOW"
        options["action_type"] = "REPLACE"
        """ 带参数调用人脸注册 """
        res=self.client.addUser(image, imageType, groupId, userId)

        return res


    # 删除人脸
    def delete(self):
        userId = "dilireba"
        groupId = "100"
        faceToken = "c6b8b4a1e359a626d4e7b4e258415c91" # 注册完人脸--》返回的
        """ 调用人脸删除 """
        res=self.client.faceDelete(userId, groupId, faceToken)
        return res

    # 搜索人脸
    def search(self):
        image = base64.b64encode(open('./gtl2.png', 'rb').read()).decode('utf-8')
        imageType = "BASE64"
        groupIdList = "100"
        """ 调用人脸搜索 """
        res=self.client.search(image, imageType, groupIdList);
        return res


if __name__ == '__main__':
    ai=BaiDuFace()
    # 注册人脸
    # res=ai.add_user()
    # # {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1689107353, 'timestamp': 1714048089, 'cached': 0, 'result': {'face_token': 'c6b8b4a1e359a626d4e7b4e258415c91', 'location': {'left': 247.62, 'top': 187.95, 'width': 170, 'height': 167, 'rotation': 0}}}
    # print(res)  # c6b8b4a1e359a626d4e7b4e258415c91

    # 删除人脸
    # {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1782556159, 'timestamp': 1714048182, 'cached': 0, 'result': None}
    # res=ai.delete()
    # print(res)

    # 搜索人脸
    # {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1871529793, 'timestamp': 1714048271, 'cached': 0,
    # 'result': {'face_token': '27fde0501d5cda5985998167a6fcb4b0', 'user_list': [{'group_id': '100', 'user_id': 'gu3tian1le4', 'user_info': '', 'score': 96.090065002441}]}}
    res=ai.search()
    print(res)