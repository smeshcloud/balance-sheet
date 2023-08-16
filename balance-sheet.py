#!/usr/bin/env python3
#
# balance-sheet.py
#
# This script will read a JSON config file and generate a balance sheet for the
# specified accounts, as well as a net worth report. It will also show the rewards
# earned for the specified smesher accounts and the total rewards earned for all,
# including pending rewards.
#

import json
import os
import sys
import time
import datetime
import argparse

import requests


# Global variables
config = None
accounts = {}
smeshers = None
explorer_api_base_url = 'https://mainnet-explorer-api.spacemesh.network/'

# Helper functions
def get_config():
  with open('config.json') as f:
    config = json.load(f)
  return config

def get_accounts():
  accounts = {}
  for address in config['accounts']:
    accounts[address] = get_account(address)
  return accounts

def get_smeshers():
  smeshers = {}
  for smesher in config['smeshers']:
    smeshers[smesher] = get_smesher(smesher)
  return smeshers

def get_account(address):
  # get account info from the API using requests
  # example uri: https://mainnet-explorer-api.spacemesh.network/accounts/sm1qqqqqqzmt7dcrfccd4n3c76q3jfnnx0fj8uuy7q22laey
  uri = explorer_api_base_url + 'accounts/' + address
  # print('Getting account info from: ' + uri)
  account = requests.get(uri).json()
  # print(account)
  if 'data' in account:
    return account["data"][0]
  else:
    return None

def get_smesher(address):
  uri = explorer_api_base_url + 'smeshers/' + address
  # print('Getting smesher info from: ' + uri)
  smesher = requests.get(uri).json()
  if 'data' in smesher:
    return smesher["data"][0]
  else:
    return None

def print_accounts(accounts):
  print('ACCOUNTS')
  for address, account in accounts.items():
    if account is None:
      print(f'{address} - account not found')
    else:
      print(f'{address} - txs: {account["txs"]}, sent: {account["sent"]}, received: {account["received"]}, awards: {account["awards"]}, fees: {account["fees"]}, balance: {account["balance"] / 1000000000} SMH')

def print_smeshers(smeshers):
  print('SMESHERS')
  for address, smesher in smeshers.items():
    if smesher is None:
      print(f'{address} - smesher not found')
    else:
      print(f'{address} - coinbase: {smesher["coinbase"]} rewards: {smesher["rewards"]}')

# Main function
def main():
  global config, accounts, smeshers
  config = get_config()

  accounts = get_accounts()
  print_accounts(accounts)
  print()

  smeshers = get_smeshers()
  print_smeshers(smeshers)


# Main entry point
if __name__ == '__main__':
  main()
