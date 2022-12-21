class SampleNotFoundError(RuntimeError):
	""" An error object of this class
	is thrown by assert_has_sample """
	pass  

class Assertions:
	def assert_has_sample(self, value):
		""" Check if value contains the word
		substring "sample". Raise a SampleNotFoundError if
		it doesn't """
		pass
