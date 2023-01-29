#!/usr/bin/env python

import json

from visify.analyzer.module_macroscopic import ModuleMacroscopic

macroscopic = ModuleMacroscopic("visify.analyzer.examples.dict")
macroscopic.run()

print(json.dumps(macroscopic.encoded_result(), indent=4))
