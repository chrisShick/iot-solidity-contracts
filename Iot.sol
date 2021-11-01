pragma solidity >=0.7.0 <0.9.0;

import "./DomainManager.sol";

contract Iot {
    // Mapping between accounts and a DomainManager address
    mapping(address => DomainManager) private domain_manager;
    
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
    }
}
