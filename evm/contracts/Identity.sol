/*
  author: @3esmit
  https://github.com/status-im/contracts/blob/master/contracts/identity/Identity.sol
*/

pragma solidity ^0.4.18;

import 'ERC725.sol';
import 'ERC735.sol'

contract Identity is ERC75, ERC735 {

  /*
    DATA STRUCTURES
  */

  struct Transaction {
    address to;
    uint256 value;
    bytes32 data;
    uin256 nonce;
  }

  /*
    STATE
  */

  mapping (address => uint256) keys;
  mapping (bytes32 => Claim) claims;
  mapping (uint256 => address[]) keysByType;
  mapping (uint256 => bytes32[]) claimsByType;
  mapping (bytes32 => uint256) indexes;
  mapping (bytes32 => Transaction) txx;

  uint256 nonce = 0;

  /*
    MODIFIERS
  */

  modifier managerOnly {
    require(keys[msg.sender] == MANAGEMENT_KEY);
    _;
  }

  modifier managerOrSelf {
    require(keys[msg.sender] == MANAGEMENT_KEY || msg.sender == address(this));
    _;
  }

  modifier actorOnly {
    require(keys[msg.sender] == ACTION_KEY);
    _;
  }

  modifier claimsSignerOnly {
    require(keys[msg.sender] == CLAIM_SIGNER_KEY);
    _;
  }

  /*
    CONSTRUCTOR
  */
  
  function Identity() public {
    _addKey(msg.sender, MANAGEMENT_KEY);
  }

  /*
    PUBLIC FNS
  */
}
