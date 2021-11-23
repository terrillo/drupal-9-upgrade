import json
import subprocess
import sys

subprocess.getoutput("rm -rf vendor composer.lock")
subprocess.getoutput("cp composer.base.json composer.json")

PROJECT = sys.argv[1]
COMPOSER = json.load(open("{}/composer.json".format(PROJECT)))
print(PROJECT)

# D9
subprocess.getoutput("composer update")

for require in COMPOSER["require"]:
    print("INSTALLING: {}".format(require))
    VERSION = COMPOSER["require"][require]
    SHELL = subprocess.getoutput("composer require {}".format(require))
    if "Problem" in SHELL:
        print(
            "{}, https://www.drupal.org/project/{}, {}".format(
                require.replace("drupal/", ""), require.replace("drupal/", ""), VERSION
            )
        )

for require in COMPOSER["require-dev"]:
    print("INSTALLING: {}".format(require))
    VERSION = COMPOSER["require-dev"][require]
    SHELL = subprocess.getoutput("composer require --dev {}".format(require))
    if "Problem" in SHELL:
        print(
            "{}, https://www.drupal.org/project/{}, {}".format(
                require.replace("drupal/", ""), require.replace("drupal/", ""), VERSION
            )
        )


NEW_COMPOSER = json.load(open("composer.json"))
for require in COMPOSER["require"]:
    VERSION = COMPOSER["require"][require]
    if require in NEW_COMPOSER["require"]:
        NEW_VERSION = NEW_COMPOSER["require"][require]
        print(
            "{}, https://www.drupal.org/project/{}, {}, {}".format(
                require.replace("drupal/", ""), require.replace("drupal/", ""), VERSION, NEW_VERSION
            )
        )

for require in COMPOSER["require-dev"]:
    VERSION = COMPOSER["require-dev"][require]
    if require in NEW_COMPOSER["require-dev"]:
        NEW_VERSION = NEW_COMPOSER["require-dev"][require]
        print(
            "{}, https://www.drupal.org/project/{}, {}, {}".format(
                require.replace("drupal/", ""), require.replace("drupal/", ""), VERSION, NEW_VERSION
            )
        )
