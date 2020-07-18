from redis import *
# # # if __name__ == '__main__':
# # #     try:
# # #         sr=StrictRedis()
# # #         result = sr.set("name","itheima")
# # #         print(result)
# # #     except Exception as e:
# # #         print(e)
# # #
# # from redis import *
# # if __name__ == '__main__':
# #     try:
# #         sr = StrictRedis()
# #         result = sr.get("name")
# #         print(result)
# #     except Exception as e:
# #         print(e)
# #
# from redis import *
# if __name__ == '__main__':
#     try:
#         sr=StrictRedis()
#         result = sr.set("name","itcast")
#         print(result)
#
#     except Exception as e:
#         print(e)
if __name__ == '__main__':
    try:
        sr = StrictRedis()
        result = sr.delete("name")

        print(result)
    except Exception as e:
        print(e)