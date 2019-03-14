# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class RetryCreateUserPasswordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'RetryCreateUserPassword','emr')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_UserInfos(self):
		return self.get_query_params().get('UserInfos')

	def set_UserInfos(self,UserInfos):
		for i in range(len(UserInfos)):	
			if UserInfos[i].get('Type') is not None:
				self.add_query_param('UserInfo.' + str(i + 1) + '.Type' , UserInfos[i].get('Type'))
			if UserInfos[i].get('GroupName') is not None:
				self.add_query_param('UserInfo.' + str(i + 1) + '.GroupName' , UserInfos[i].get('GroupName'))
			if UserInfos[i].get('UserId') is not None:
				self.add_query_param('UserInfo.' + str(i + 1) + '.UserId' , UserInfos[i].get('UserId'))
			if UserInfos[i].get('UserName') is not None:
				self.add_query_param('UserInfo.' + str(i + 1) + '.UserName' , UserInfos[i].get('UserName'))
