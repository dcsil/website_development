import spacy

nlp = spacy.load('en_core_web_md')
from collections import OrderedDict


# python -m spacy download en_core_web_md

# get sorted video tags from influencer info
def get_tags(influ_info: dict):
    tags = OrderedDict()
    for video in influ_info['video_list']:
        for label in video["label_list"]:
            if label not in tags:
                tags[label] = 0
            tags[label] += 1

    tags = {k: v for k, v in
            sorted(tags.items(), key=lambda item: item[1], reverse=True)[:5]}
    return tags


def text_similarity(phase1, phase2):
    # words = f"{word1} {word2}"
    # tokens = nlp(words)
    # token1, token2 = tokens[0], tokens[1]
    # print("Similarity:", token1.similarity(token2))
    doc1 = nlp(phase1)
    doc2 = nlp(phase2)
    return doc1.similarity(doc2)


def match_influ_tags(search_tag: str, video_tags: dict):
    score = 0
    total = 0
    for tag, count in video_tags.items():
        # if count > 5:
        s = text_similarity(search_tag, tag)
        if s > 0.5:
            return s
        score += s * count
        total += count
        # else:
        #     break
    if total == 0:
        return 0
    return score / total


def get_match_influ(search_tag: str, all_influ: list):
    match_list = []
    score_list = []
    total = 0
    index = 0
    for influ in all_influ:
        tags = get_tags(influ)
        score = match_influ_tags(search_tag, tags)
        # if score > 0.3:
        #     match_list.append(index)
        score_list.append((index, score))
        index += 1
        total += score

    ave = total / index
    score_list = sorted(score_list, key=lambda item: item[1], reverse=True)
    for (i, score) in score_list:
        if score > max(ave, 0.2):
            match_list.append(all_influ[i])
        else:
            break
    return match_list


if __name__ == '__main__':
    pass
    # # sample_influ = get_one_influencer("afrae.es")
    # influs = get_all_influencer()
    # search_tag = "game"
    # match_list = get_match_influ(search_tag, influs)
    #
    # for sample_influ in match_list:
    #     tags = get_tags(sample_influ)
    #     print(f"Tags: {tags}\n")
