pragma solidity >=0.7.0 <0.9.0;

import "./Iot.sol";
import "./Domain.sol";

contract DomainManager {
    
    // Reference to the owner of the DomainManager
    address private owner;
    
    // Reference to the Iot contract that created this DomainManager
    Iot private parentContract;

    
    // Mapping between an address of account that represents a domain
    mapping(address => Domain) private domains;
    
    /**
     * DomainManager is created with the parentContract being passed
     * in and the account address that is creating the domain.
     * 
     **/
    constructor(Iot _parentContract, address _account) {
        parentContract = _parentContract;
        owner = _account;
    }
   
   /**
    * Modifier to ensure that only a particular address can
    * call the particular the modifier is attached to.
    * 
    **/
    modifier onlyBy(address _account) {
        require(
            msg.sender == _account,
            "Sender not authorized."
        );
        _;
    }
    
    /**
     * Allow only the set owner to add domains
     **/
    function registerDomain(address _domainKey) public onlyBy(owner) {
        Domain d = new Domain(this, _domainKey);
        
        domains[_domainKey] = d;
    }
    
    /**
     * Get a domain by address
     * 
     **/
    function getDomain(address _domainKey) public view returns(Domain) {
        return domains[_domainKey];
    }
}
