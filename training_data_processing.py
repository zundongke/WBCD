import numpy as np
import pathlib as path
from abc import ABC, abstractmethod
import h5py
class read_episode():
    def __init__(self,pth: path) -> None:
        with h5py.File(pth, 'r') as f:
            self.action=f['action'][()]
            self.qvel=f['observation/qvel'][()]
            self.qpos=f['observation/qpos'][()]


class processing_delta():
    def __init__(self,path):
        self.path=path
        self.reader=read_episode(path)
    def processing(self):
        self.qvel=self.reader.qvel
        self.qpos=self.reader.qpos
        self.action=np.array(self.reader.action)
        for i in self.action.shape[0]:
            self.action[i+1]=self.action[i+1]-self.action[i]
        self.action[0]=0

    def save_data(self):
        with h5py.File(self.path, 'r') as f:
            pass
class processing_chunking():
    def __init__(self,path,k):
        self.reader=read_episode(path)
        self.k=k
        self.path=path
    def processing(self,k):
        self.qvel=self.reader.qvel
        self.qpos=self.reader.qpos
        self.action=np.array(self.reader.action)
        for i in range(0,self.action.shape[0],self.k):
            for j in range(self.k):
                self.action[i+j+1]=self.action[i+j+1]-self.action[i]
        self.action[0]=0
    def save_data(self):
        with h5py.File(self.path, 'r') as f:
            pass