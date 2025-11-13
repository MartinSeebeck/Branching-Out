
import json
import os

userfile_path =  './users.json'

def filter_users_by_name(name):
	try: #make sure that file exists
		with open("users.json", "r") as file:
			users = json.load(file)
			filtered_users = [user for user in users if user["name"].lower() == name.lower()]
			#return result as listing
			for user in filtered_users:
				print(user)
			return filtered_users #for possible later save
	except FileNotFoundError as err:
		print(f"The attempt to open {userfile_path} has resulted in the following error message:")
		print(err)


def filter_users_by_age(age):
	with open("users.json", "r") as file:
		users = json.load(file)

	filtered_users = [user for user in users if user["age"] == age]

	for user in filtered_users:
		print(user)
	return filtered_users #for possible later save

def filter_users_by_email(email):
	with open("users.json", "r") as file:
		users = json.load(file)

	filtered_users = [user for user in users if user["email"] == email]

	for user in filtered_users:
		print(user)
	return filtered_users #for possible later save

def save_results_to_file(result_filtered_users):
	save_to_file = input("Enter y to save the result to file 'results.txt', any other input will abort: ")
	if save_to_file == "y":
		stringed_result = str(result_filtered_users)
		with open("results.txt", "w") as file:
			file.write(stringed_result)


if __name__ == "__main__":
	if os.path.exists(userfile_path):
		filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()
		if filter_option == "name":
			name_to_search = input("Enter a name to filter users: ").strip()
			result_filtered_users = filter_users_by_name(name_to_search)
			if not result_filtered_users == []:
				save_results_to_file(result_filtered_users)
			else:
				print("The search returned no qualified entry.")

		elif filter_option == "age":
			age_to_search = input("Enter an age to filter users: ")
			try:
				int_age_to_search = int(age_to_search)
			except ValueError as err:
				print(f"The input has returned error message: '{err}'")
				print("Please input numerical characters only.")
			result_filtered_users = filter_users_by_age(int_age_to_search)
			if not result_filtered_users == []:
				save_results_to_file(result_filtered_users)
			else:
				print("The search returned no qualified entry.")

		elif filter_option == "email":
			string_to_search = input("Enter an email address to filter users: ").strip()
			lower_string_to_search = string_to_search.lower()
			result_filtered_users = filter_users_by_email(lower_string_to_search)
			if not result_filtered_users == []:
				save_results_to_file(result_filtered_users)
			else:
				print("The search returned no qualified entry.")

		else:
			print("Filtering by that option is not yet supported.")

	else:
		print("The user database 'users.json' appears to be missing and/or corrupted.")
		print("Please check with an administrator.")


