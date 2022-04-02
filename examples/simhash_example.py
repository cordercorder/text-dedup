#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-04-02 12:54:28
# @Author  : Chenghao Mou (mouchenghao@gmail.com)

from text_dedup.embedders.simhash import SimHashEmbedder
from text_dedup.utils.nn import simhash_clustering
from text_dedup.utils.group import get_group_indices

if __name__ == "__main__":

    corpus = [
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy dog",
        "This is a test",
        "This is a test",
    ]

    embedder = SimHashEmbedder()
    embeddings = embedder.embed(corpus)

    clusters = simhash_clustering(embeddings)
    groups = get_group_indices(clusters)
    print(groups)