#coding:utf-8
import json

with open("parameter.json","r",encoding='utf-8') as f:
  d = json.load(f)

no = d['no']
token = d['token']
if ('Authorization' in d):
  Authorization = d['Authorization']
if ('serial_no' in d):
  serial_no = d['serial_no']
if ('rno' in d):
  rno = d['rno']