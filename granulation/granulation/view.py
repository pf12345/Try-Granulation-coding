# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import json
from bson.objectid import ObjectId

import orgStructure

def getOrgstructure(request):
	return HttpResponse(json.dumps({"result": "ok", "data": orgStructure.ORGSTRUCTURE}), content_type="application/json")