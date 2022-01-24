# Databricks notebook source
# DBTITLE 1,Install nutter and it's dependencies
# MAGIC %pip install nutter

# COMMAND ----------

# DBTITLE 1,Define testing classes  
from runtime.nutterfixture import NutterFixture, tag


class HistoryDataTestFixture(NutterFixture):
    def run_test_name(self):
        print("Tested the code")

    def assertion_test_name(self):
        assert 2 > 1


result = HistoryDataTestFixture().execute_tests()
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

