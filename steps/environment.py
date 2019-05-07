# -*- coding: UTF-8 -*-
from behave import use_fixture
import os.path
import json

def before_all(context):
	context.config.setup_logging()
	# -- ALTERNATIVE: Setup logging with a configuration file.
	context.config.setup_logging(configfile="behave_logging.ini")
	userdata = context.config.userdata
	configfile = userdata.get("configfile", "userconfig.json")
	if os.path.exists(configfile):
		assert configfile.endswith(".json")
		more_userdata = json.load(open(configfile))
		context.config.update_userdata(more_userdata)
		count = userdata.getint("count", 100)
		server = userdata.get("server", "asterix")
		print(count)
		print(server)
	
def before_scenario(context, scenario):
	print("With Before Scenario")

def after_scenario(context, scenario):
	print("With After Scenario")

def before_tag(context, tag):
	if tag == "WINDOWS":
		print("Before Windows Tag")
	if tag == "Linux":
		print("Before Linux Tag")
	
def after_tag(context, tag):
	if tag == "WINDOWS":
		print("After Windows Tag")
	if tag == "Linux":
		print("After Linux Tag")
	

