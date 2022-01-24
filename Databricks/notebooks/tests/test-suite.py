# Databricks notebook source
# DBTITLE 1,Install nutter and it's dependencies
# MAGIC %pip install nutter

# COMMAND ----------

# Define testing classes 
from runtime.nutterfixture import NutterFixture, tag

#This Suite class is to test all the notebooks that are creaetd in the workspace.
class SuiteTestFixture(NutterFixture):
    def run_test_history(self):
        dbutils.notebook.run("../src/history/historynb", 600)

    def assertion_test_history(self):
        print("Assertion Logic for History notebook to be added here")
        assert 2 > 1

    def run_test_config(self):
        dbutils.notebook.run("../src/config/confignb", 600)

    def assertion_test_config(self):
        print("Assertion Logic for config notebook to be added here")
        assert 2 > 1

result = SuiteTestFixture().execute_tests()
print(result.to_string())

is_job = (
    dbutils.notebook.entry_point.getDbutils()
    .notebook()
    .getContext()
    .currentRunId()
    .isDefined()
)
if is_job:
    result.exit(dbutils)

