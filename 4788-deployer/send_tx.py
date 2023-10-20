import os
import logging
from web3 import Web3
import argparse

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

VALUE_TO_SEND = "0x9184"
receiver = "0x0B799C86a49DEeb90402691F1041aa3AF2d3C875"

def send_transaction(sender_private_key, el):
  w3 = Web3(Web3.HTTPProvider(el))
  sender_account = w3.eth.account.from_key(sender_private_key)
  block = w3.eth.get_block('latest')
  if block.number > 1:
    value_in_wei = int(VALUE_TO_SEND, 16)
    transaction = {
      "from": sender_account.address,
      "to": receiver,
      "value": value_in_wei,
      "gasPrice": w3.eth.gas_price,
      "nonce": w3.eth.get_transaction_count(sender_account.address)
    }
    estimated_gas = w3.eth.estimate_gas(transaction)
    transaction["gas"] = estimated_gas
    signed_txn = sender_account.sign_transaction(transaction)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"Transaction hash: {tx_hash.hex()}")
    logging.info(f"Sender balance: {w3.eth.get_balance(sender_account.address)}")
    logging.info(f"Receiver balance: {w3.eth.get_balance(receiver)}")

def main():
  parser = argparse.ArgumentParser(description='Send Ethereum transaction')
  parser.add_argument('--privateKey', type=str, default=None, help='Sender private key')
  parser.add_argument('--el', type=str, default=None, help='Execution layer URI')
  args = parser.parse_args()
  private_key = args.privateKey
  el = args.el
  if private_key is None or args.el is None:
    parser.print_help()
    return
  logging.info("Sending transaction...")
  send_transaction(private_key, el)
  logging.info("Transaction sent.")

if __name__ == "__main__":
    main()