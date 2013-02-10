import yaml
import types

class Settings:

   def __init__(self, module):
		if type(module) == file:
			module = yaml.load(module)
		else:
			module = module.__dict__
		self.manglers = module.get('MANGLERS', {})
		self.servers = module.get('SERVERS', {})

   def _createClasses(self, names):
      result = []
      for classname, arguments in names.iteritems():
         if type(classname) == types.InstanceType:
            result.append(classname)
            continue
         parts = classname.split('.')
         module = __import__('.'.join(parts[:-1]))
         for part in parts[1:]:
            module = getattr(module, part)
         if arguments:
            result.append(module(**arguments))
         else:
            result.append(module())
      return result

   def getManglers(self):
      return self._createClasses(self.manglers)

   def getServers(self):
      return self._createClasses(self.servers)

