import json
from pprint import pprint


def get_qa_data(path):
    """
    sentences：(问句， 答案)
    :param path:
    :return:
    """
    with open(path, 'r') as fp:
        data = fp.read()
    data = json.loads(data)
    sentences = []
    for k,v in data.items():
        question = v['question']
        evidences = v['evidences']

        answer = []
        for p,q in evidences.items():
            if q['answer'] != ['no_answer'] and q['answer'][0] not in answer:
                answer.append(q['answer'][0])
        sentences.append((question, "".join(answer)))
    return sentences



if __name__ == '__main__':
    path = './WebQA.v1.0/me_train.json'
    get_qa_data(path)