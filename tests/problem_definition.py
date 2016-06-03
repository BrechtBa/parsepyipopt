#!/usr/bin/env/ python
################################################################################
#    Copyright 2016 Brecht Baeten
#    This file is part of jsonopt.
#
#    jsonopt is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jsonopt is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with jsonopt.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import unittest

import jsonopt

class TestProblemDefinition(unittest.TestCase):

	def test_create_empty_problem(self):
		problem = jsonopt.Problem()
	
	def test_add_variable(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x')
		self.assertEqual(len(problem.model.x),1)
		
	def test_add_variable_array(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x[j] for j in range(25)')
		self.assertEqual(len(problem.model.x),25)
		
	def test_add_variable_ndarray(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x[i,j,k] for i in range(2) for j in range(3) for k in range(4)')
		self.assertEqual(len(problem.model.x),2*3*4)
		
	def test_add_variable_with_initial_value(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x=3')
		self.assertEqual(problem.model.x.value,3)

	def test_add_variable_array_with_initial_value(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x[j] = 3*j for j in range(25)')
		self.assertEqual([problem.model.x[j].value for j in range(25)],[3*j for j in range(25)])
	
	def test_add_variable_ndarray_with_initial_value(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x[i,j,k] = 1 if i==0 else 2 for i in range(2) for j in range(3) for k in range(4)')
		self.assertEqual([problem.model.x[i,j,k].value for i in range(2) for j in range(3) for k in range(4)],[1 if i==0 else 2 for i in range(2) for j in range(3) for k in range(4)])
	
	def test_add_variable_ndarray_with_initial_value_sum(self):
		problem = jsonopt.Problem()
		problem.add_variable('Reals x[i,j,k] = sum(a+b for a in range(i+2) for b in range(j+2)) for i in range(2) for j in range(3) for k in range(4)')
		self.assertEqual([problem.model.x[i,j,k].value for i in range(2) for j in range(3) for k in range(4)],[sum(a+b for a in range(i+2) for b in range(j+2)) for i in range(2) for j in range(3) for k in range(4)])
		
if __name__ == '__main__':
	unittest.main()