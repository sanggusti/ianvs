# From icyfeather sample of singletask learning of simple qa

from sedna.common.class_factory import ClassType, ClassFactory

__all__ = ["acc"]

def get_last_letter(input_string):
    # 检查输入是否为空或只包含非字母字符
    if not input_string or not any(char.isalpha() for char in input_string):
        return None

    # 倒序遍历字符串，找到最后一个字母
    for char in reversed(input_string):
        if 'A' <= char <= 'D':
            return char

    # 如果没有找到字母，返回None
    return None

@ClassFactory.register(ClassType.GENERAL, alias="acc")
def acc(y_true, y_pred):
    y_pred = [get_last_letter(pred) for pred in y_pred]
    print(y_true)
    print(y_pred)
        
    # 使用列表推导来比较两个列表中的元素是否相同
    same_elements = [y_pred[i] == y_true[i] for i in range(len(y_pred))]

    # 计算相同元素的数量
    acc = sum(same_elements) / len(same_elements)
    
    return acc