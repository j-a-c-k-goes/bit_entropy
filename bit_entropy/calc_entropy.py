# - - - module imports - - -
import math
import hashlib
import secrets

# - - - generate a test hash value - - -
def create_test_hash_value():
	# - - - crypto random value - - -
	rand_hash_value = secrets.token_hex(32)
	# - - - bind hashed value  - - -
	hashed_value = hashlib.sha256()
	# - - - bind digest of hashed value  - - -
	digested_value = hashed_value.digest()
	safe_digest = hashed_value.hexdigest()
	# - - - create string of digest, currently an object - - -
	hash_to_hex_string =  hashlib.sha256().hexdigest()
	return { 
		# - - - key_hashed  - - -
		'test_hash': rand_hash_value, 
		# - - - key_digest  - - -
		'digested_hash': safe_digest }

# - - - do math for bit entropy - - -
# - - - update to support upper,lower,latin characters  - - -
def calc_bit_entropy(hash_value):
	hash_value = hash_value.strip()
	len_of_hash = len(hash_value)
	entropy = math.pow(2, len_of_hash)
	return entropy

# - - - generate a set of test hash values - - -
def make_test_value_set():
	_set = []
	for i in range(100):
		test_values = create_test_hash_value()
		_set.append(test_values)
	return _set

# - - - print set of test values - - -
def print_test_values(test_values):
	[print(value, "\n") for value in test_values]

# - - - on run and module export - - -
if __name__ == "__main__":
	test_value = create_test_hash_value()
	test_values = make_test_value_set()
	bit_entropy = calc_bit_entropy(test_value['test_hash'])
	# - - - print statement - - -
	print(
f"""	
test hash: {test_value['test_hash']}
test digest: {test_value['digested_hash']}
bit entropy: {bit_entropy}
""")
