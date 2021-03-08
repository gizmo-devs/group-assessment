# ECM1421 Group Assessment

This is for the group assignment for ECM1421.

## How to pull down the repository
1. open terminal and go to directory where you would like to the repository to be stored
2. `git clone https://github.com/GizmoStudent/group-assessment.git`
3. cd `group-assessment`

## Running the application
1. navigate to the repository
2. `python check_crime.py`

Note: all files (crimes + postcodes) are located in the `./app/data_files` directory

## Making contributions
__No changes are to be made to the `main` branch__.

Create a new branch using the naming convention:
- feature/[Feature_name]
  - For creating code and functions
- docs/[Feature_name]
  - for updating the documentation on features.
- All new modules should be created in the `./app/custom_modules/` directory.
- For the application logic (i.e. asking for input or activating module functions), this is to be done in the `./app/main.py` file.
- All other logic and tests are to be done in the module itself.

## Tests
At the bottom of your `custom_modules` file should contain a condition statement:
```python
if __name__ == '__main__':
    assert a_test_function() == "Output Value", "Output value did not match the value returned from function"
```