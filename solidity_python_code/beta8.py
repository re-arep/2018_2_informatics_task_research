import json
import web3

from web3 import Web3, HTTPProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.8;

// 본인 확인 계약
contract PersonCertification {
    // 계약 관리자 주소
    address admin;
    
    // 열람 허가 정보
    struct AppDetail {
        bool allowReference;
        uint256 approveBlockNo;
        uint256 refLimitBlockNo;
        address applicant;
    }
    
    // 본인 확인 정보
    struct PersonDetail {
        string name;
        string birth;
        address[] orglist;
    }
    
    //인증 기관 정보(학교, 회사 등)
    struct OrganizationDetail {
        string name;
    }
    
    // 해당 키의 열람 허가 정보
    mapping(address => AppDetail) appDetail;
    
    // 해당 키의 본인 확인 정보
    mapping(address => PersonDetail) personDetail;
    
    // 해당 키의 조직 정보
    mapping(address => OrganizationDetail) public orgDetail;
    
    // 생성자
    function PersonCertification() {
        admin = msg.sender;
    }
    
    // ---------------------
    // 데이터 등록 기관(set)
    // ---------------------
    
    // 본인 정보를 등록
    function setPerson(string _name, string _birth) {
        personDetail[msg.sender].name = _name;
        personDetail[msg.sender].birth = _birth;
    }
    
    // 조직 정보를 등록
    function setOrganization(string _name) {
        orgDetail[msg.sender].name = _name;
    }
    
    // 조직이 개인의 소속을 증명
    function setBelong(address _person) {
        personDetail[_person].orglist.push(msg.sender);
    }
    
    // 본인 확인 정보 참조를 허가
    function setApprove(address _applicant, uint256 _span) {
        appDetail[msg.sender].allowReference = true;
        appDetail[msg.sender].approveBlockNo = block.number;
        appDetail[msg.sender].refLimitBlockNo = block.number + _span;
        appDetail[msg.sender].applicant = _applicant;
    }
    
    // ---------------------
    // 데이터 취득 함수(set)
    // ---------------------
    
    // 본인 확인 정보를 참조
    function getPerson(address _person) public constant returns(bool _allowReference, uint256 _approveBlockNo, uint256 _refLimitBlockNo, address _applicant, string _name, string _birth, address[] _orglist) {
        // 열람을 허가할 정보
        _allowReference = appDetail[_person].allowReference;
        _approveBlockNo = appDetail[_person].approveBlockNo;
        _refLimitBlockNo = appDetail[_person].refLimitBlockNo;
        _applicant = appDetail[_person].applicant;
        
        // 열람을 제한할 정보
        if (((msg.sender == _applicant) && (_allowReference == true) && (block.number < _refLimitBlockNo)) || (msg.sender == admin) || (msg.sender == _person)) {
            _name = personDetail[_person].name;
            _birth = personDetail[_person].birth;
            _orglist = personDetail[_person].orglist;
        }
    }
}
'''

#Web3 setting
rpc_url = "http://localhost:8545"
w3 = Web3(HTTPProvider(rpc_url))

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Compiled source code
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Greeter']

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'],
                          bytecode=contract_interface['bin'])

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)
