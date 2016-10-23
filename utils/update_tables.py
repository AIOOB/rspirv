#!/usr/bin/env python2
# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Updates various tables generated from SPIR-V grammar."""

import os
import imp

directory = os.path.dirname(os.path.realpath(__file__))

script = imp.load_source('gen_tables',
                         os.path.join(directory, 'gen_grammar_tables.py'))

src = os.path.join(directory, '..', 'rspirv')
grammar_input = os.path.join(src, 'external/spirv.core.grammar.json')
operand_parse_output = os.path.join(src, 'binary/parse_operand.rs')

script.update(grammar_input, operand_parse_output)
