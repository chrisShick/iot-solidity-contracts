pragma solidity >=0.7.0 <0.9.0;
//SPDX-License-Identifier: MIT

import "./Domain.sol";

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/ECDSA.sol";

contract Device {

    enum RegistrationState{ UNREGISTERED, REGISTERED }
    enum DeviceState{ ACTIVE, INACTIVE }

    // Future public key once the device is registered
    address private owner;
    // Index within the parent contract
    uint256 index;

    // Parent Contract reference
    Domain parentContract;

    // Current registration state of the device
    RegistrationState private currentRegistrationState;

    // Current state of the device
    DeviceState private currentDeviceState;


    event DeviceRegistered(address indexed _device, address indexed _account);

    /**
    * Modifier to ensure that only a particular address can
    * call the particular the modifier is attached to.
    *
    **/
    modifier onlyActive() {
        require(
            currentDeviceState == DeviceState.ACTIVE,
            "Device not active."
        );
        _;
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

    constructor(Domain _parentContract, uint256 _index) {
        parentContract = _parentContract;
        index = _index;
    }

    /**
     * Register the public key address by verifying the signature generated
     * offchain.
     **/
    function register(/*bytes memory _signature*/) public onlyActive {
        require(
            currentRegistrationState != RegistrationState.UNREGISTERED,
            "Device Already Registered"
        );

        // TODO: VALIDATE SIGNATURE AND ASSIGN TO publicKey variable
        owner = msg.sender;
        
        emit DeviceRegistered(address(this), address(owner));
    }
}
