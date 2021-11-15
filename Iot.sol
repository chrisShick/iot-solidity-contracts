pragma solidity >=0.7.0 <0.9.0;
// SPDX-License-Identifier: MIT

import "./DomainManager.sol";

contract Iot {
    // Mapping between accounts and a DomainManager address
    mapping(address => DomainManager) private domain_manager;

    event AccountRegistered(address indexed _from, address indexed _domainManager);

    /**
     * This function allows an account to register a domain under there account address.
     *
     * TODO:
     *    1. Do a check to only allow 1 DomainManager to an account
     *
     **/
    function registerDomain() public {
        DomainManager ds = new DomainManager(this, msg.sender);
        domain_manager[msg.sender] = ds;

        emit AccountRegistered(msg.sender, address(ds));
    }

     /**
     * This function returns address of domain manager.
     *
     *
     **/
    function getDomainManager() public view returns(address) {
        return address(domain_manager[msg.sender]);
    }
}
