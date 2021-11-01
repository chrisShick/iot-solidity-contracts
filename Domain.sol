pragma solidity >=0.7.0 <0.9.0;

import "./DomainManager.sol";
import "./Device.sol";

contract Domain {
    // States of the domain
    enum State{ ACTIVE, INACTIVE }
    
    // Reference to the owner of the DomainManager
    address private owner;

    // Reference to the address of the parentContract
    DomainManager private parentContract;
    
    // Current state of the domain
    State private currentState;

    // Mapping of devices
    mapping(uint256 => Device) private devices;
    uint256 index;
    
    constructor(DomainManager _parentContract, address _publicKey) {
        parentContract = _parentContract;
        owner = _publicKey;
        currentState = State.ACTIVE;
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
    * Modifier to ensure that only a particular address can
    * call the particular the modifier is attached to.
    * 
    **/
    modifier onlyActive() {
        require(
            currentState == State.ACTIVE,
            "Domain not active."
        );
        _;
    }
    
    event DomainDeactived(address indexed _domain);
    event DeviceAdded(address indexed _domain, address indexed _device);

    /**
     * Deactive domain to make it in elgible for verification purposes
     **/
    function deactive() public onlyBy(owner) onlyActive {
        currentState = State.INACTIVE;
        emit DomainDeactived(address(this));
    }
    
    function addDevice(bytes32 nonce) public onlyBy(owner) onlyActive {
        Device d = new Device(this, index, nonce);
        devices[index] = d;
        index++;
        
        emit DeviceAdded(address(this), address(d));
    }
}
