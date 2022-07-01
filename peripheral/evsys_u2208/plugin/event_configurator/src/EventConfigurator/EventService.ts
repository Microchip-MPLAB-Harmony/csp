import { GetSymbolValue, GetSymbolArray, UpdateSymbolValue, clearSymbol, AddSymbolListener } from '../Common/SymbolAccess';
import {component_id} from './UI/MainView/MainBlock'

let MAX_CHANNELS = -1;
let MAX_USERS = -1;
let userNameIndexsMap = new Map<string, number>();

export function GetMaxChannels() :number{
    if (MAX_CHANNELS === -1) {
        MAX_CHANNELS = GetSymbolValue(component_id, "EVSYS_CHANNEL_NUMBER")       
    }     
    return MAX_CHANNELS;
}

export function GetMaxUsers() :number{
    if (MAX_USERS === -1) {
        MAX_USERS = GetSymbolValue(component_id, "EVSYS_USER_NUMBER");
    }
    return MAX_USERS;
}

export function registerForChannelUpdateCallback() {    
    const maxChannels:number = GetMaxChannels();
    for (let channelId = 0; channelId < maxChannels; channelId++) {
        let symbolId = "EVSYS_CHANNEL_"+channelId;
        AddSymbolListener(symbolId);        
    }
    
}

export function registerForUsersUpdateCallback() {    
    const maxUsers:Number = GetMaxUsers();
    for (let user = 0; user < maxUsers; user++) {
        let symbolId = "EVSYS_USER_"+user;
        AddSymbolListener(symbolId);        
    }    
}

export function getEnabledChannelList(): string[] {
    const maxChannels:Number = GetMaxChannels();
    let eventChannelList: string[]  = [];
    for (let channelId = 0; channelId < maxChannels; channelId++) {
        let symbolId = "EVSYS_CHANNEL_"+channelId;        
        let value:String = GetSymbolValue(component_id, symbolId);        
        if (value.toLowerCase() === "true") {
            eventChannelList.push("CHANNEL_"+channelId);
        }
    }
    return eventChannelList;
}

export function enableNextAvailableChannel():string {
    let availableChannel:string = "";
    const maxChannels:Number = GetMaxChannels();
    for (let channelId = 0; channelId < maxChannels; channelId++) {
        let symbolId = "EVSYS_CHANNEL_"+channelId;        
        let value:String = GetSymbolValue(component_id, symbolId);        
        if (value.toLowerCase() !== "true") {
            enableDisableChannel(symbolId, true);
            availableChannel = symbolId;
            break;
        }
    }
    return availableChannel;
}

export function enableDisableChannel(chnlId:string, enable:boolean) {
    let chnlNum: string = chnlId.replace(/^\D+/g, "");
    UpdateSymbolValue(component_id, "EVSYS_CHANNEL_"+chnlNum, enable);
    if (!enable) {
        clearSymbol(component_id, chnlId);
    }
}

export function getUserNameIndexMap():Map<string, number> {    
    if (userNameIndexsMap.size === 0) {
        const users:String[] = GetSymbolArray(component_id, "EVSYS_USERS");
    
        users.forEach((item)=> {
            let splitString = item.split('-');       
            userNameIndexsMap.set(splitString[0], +splitString[1]);  
        })
    }
    
    return userNameIndexsMap;
}

export function GetUsersData(): { symId:string, key: string, chnl:string}[] {
    let usersData:{symId:string, key: string , chnl:string}[] = [];
    let userNameIndexsMap = getUserNameIndexMap();
    
    const MAX_USERS = GetMaxUsers();   

    let count:number = 0;
    userNameIndexsMap.forEach((value:number, key:string)=>{
        if (count >= MAX_USERS ) {            
            return false;
        }
        count++;
   
        let symId:string = "EVSYS_USER_" + value;        
        let chnl = GetSymbolValue(component_id, symId)
        if (chnl !== 'NONE' && chnl !== undefined) {            
            usersData.push({symId: symId , key: key , chnl:chnl});
        }
    })
    
    return usersData;
}

export function addUser(): boolean {
    console.log("add User: 1");
    if (getEnabledChannelList().length <= 0) {
        return false;
    }
    console.log("add User: 2");
    let usrNameIdxsMap = getUserNameIndexMap();
    console.log("add User: 3 usrNameIdxsMap: "+ usrNameIdxsMap.size);
    for (let i=0; i < usrNameIdxsMap.size; i++) {
        let symId = "EVSYS_USER_"+ i;
        let chnl = GetSymbolValue(component_id, symId);
        console.log("add User: 4 chnl: "+ chnl);
        if (chnl === undefined || chnl === 'NONE') {
            UpdateSymbolValue(component_id, symId, "CHANNEL_0");
            console.log("add User: 3");
            return true;
        }
    }    
    return false;
}

export function getAllChannels() :string[]{
    return GetSymbolArray(component_id, getInitialUserSymbolId());
}

function getInitialUserSymbolId():string {
    return getValidSymbolId("EVSYS_USER_", 0, "", GetMaxUsers());
}

function getValidSymbolId(startSymbolID:string, nIntialIndex: number,
    endSymbolID:string, nMaxIndex:number) {
    let symbolID = '';
    for (let i = nIntialIndex; i < nMaxIndex; i++) {
        symbolID = startSymbolID + i + endSymbolID;
        let value = GetSymbolValue(component_id, symbolID);
        if (value != null) {
            return symbolID;
        }
    }
    return symbolID;
}