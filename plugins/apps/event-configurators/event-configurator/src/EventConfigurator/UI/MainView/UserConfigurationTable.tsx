import React, { useState, useEffect } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { component_id } from './MainBlock';
// import {
//   GetSymbolValue,
//   GetSymbolArray,
//   UpdateSymbolValue,
//   clearSymbol,
//   IsTrustZoneSupported,
//   AddSymbolListener,
// } from "Common/SymbolAccess";

import {
  GetSymbolValue,
  GetSymbolArray,
  UpdateSymbolValue,
  clearSymbol,
  AddSymbolListener,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import { IsTrustZoneSupported } from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';
import { Dropdown as PrimeDropDown } from 'primereact/dropdown';
import { getEnabledChannelList, getUserNameIndexMap } from '../../EventService';
import { PrimeIcons } from 'primereact/api';
// import { convertToBoolean } from "Common/Utils";
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
// import { globalSymbolSStateData } from "Common/UIComponents/UIComponentCommonUtils";
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

interface UserData {
  userData: { symId: string; key: string; chnl: string }[];
  onRemoveUser: (symId: string) => void;
  onTableDataUpdate: () => void;
}

const UserTable = (props: UserData) => {
  let modifiedKeysList: string[] = [];
  let trustzoneSupported = convertToBoolean(IsTrustZoneSupported());

  function GetTrustZoneClassName(value: any) {
    if (value === 'SECURE') {
      return 'secure';
    }
    return 'nonsecure';
  }

  props.userData.forEach((item) => modifiedKeysList.push(item.key));

  function getKeyList(rowKey: string) {
    let keysList: string[] = [];
    keysList.push(rowKey);
    getUserNameIndexMap().forEach((value, key) => {
      if (!modifiedKeysList.includes(key)) {
        keysList.push(key);
      }
    });

    return keysList;
  }

  const User = (rowData: { symId: string; key: string; chnl: string }) => {
    let [selectedUser, setSelectedUser] = useState<String>(rowData.key);

    const updateValue = (event: { value: any }) => {
      console.log(event.value);
      const userIndex: number | undefined = getUserNameIndexMap().get(
        event.value
      );
      if (userIndex !== undefined) {
        let value: string = GetSymbolValue(component_id, rowData.symId);
        UpdateSymbolValue(
          component_id,
          'EVSYS_USER_' + userIndex.toString(),
          value
        );
        UpdateSymbolValue(component_id, rowData.symId, 'NONE');
        clearSymbol(component_id, rowData.symId);
      }

      selectedUser = event.value;
    };

    useEffect(() => {
      setSelectedUser(rowData.key);
    }, [rowData]);

    return (
      <div>
        <PrimeDropDown
          id={rowData.symId}
          style={{}}
          value={selectedUser}
          options={getKeyList(rowData.key)}
          disabled={false}
          onChange={(e) => updateValue(e)}
        />
      </div>
    );
  };

  const ChannelNumber = (rowData: {
    symId: string;
    key: string;
    chnl: string;
  }) => {
    let channelList: string[] = [];
    let [selectedChnl, setSelectedchnl] = useState<String>(rowData.chnl);

    useEffect(() => {
      setSelectedchnl(rowData.chnl);
    }, [rowData]);

    getEnabledChannelList().forEach((item) => {
      channelList.push(item);
    });

    const channelUpdate = (event: { value: any }) => {
      UpdateSymbolValue(component_id, rowData.symId, event.value);
      // selectedChnl = event.value;
      setSelectedchnl(event.value);
      console.log(selectedChnl);
    };

    return (
      <PrimeDropDown
        id={rowData.symId}
        style={{}}
        value={selectedChnl}
        options={channelList}
        disabled={false}
        onChange={(e) => channelUpdate(e)}
      />
    );
  };

  const SecurityMode = (rowData: {
    symId: string;
    key: string;
    chnl: string;
  }) => {
    const userId: string = rowData.symId.replace(/^\D+/g, '');
    const symbol = 'EVSYS_USER_NONSEC_' + userId;

    const changeComponentstate = (
      value: any,
      editable: boolean,
      visible: boolean
    ) => {
      alert('changed Value' + value);
      setSelectedMode(value);
    };

    let [selectedMode, setSelectedMode] = useState<String>(() => {
      alert('register listener: ' + symbol);
      globalSymbolSStateData.set(symbol, {
        changeComponentState: changeComponentstate,
      });
      AddSymbolListener(symbol);
      return GetSymbolValue(component_id, symbol);
    });

    useEffect(() => {
      setSelectedMode(GetSymbolValue(component_id, symbol));
    }, [rowData]);

    function ConfigurationChanged(event: { value: any }) {
      UpdateSymbolValue(component_id, symbol, event.value);
      setSelectedMode(event.value);
    }

    return (
      <div className="p-d-flex secure-combo">
        <PrimeDropDown
          id={rowData.symId}
          style={{}}
          value={selectedMode}
          options={GetSymbolArray(component_id, symbol)}
          disabled={false}
          onChange={(e) => ConfigurationChanged(e)}
          className={GetTrustZoneClassName(
            GetSymbolValue(component_id, symbol)
          )}
        />
      </div>
    );
  };

  const RemoveUser = (rowData: any) => {
    return (
      <div
        className={PrimeIcons.TRASH}
        onClick={(e) => {
          props.onRemoveUser(rowData.symId);
        }}
      ></div>
    );
  };

  return (
    <div>
      <div className="card">
        <DataTable
          value={props.userData}
          stripedRows
          size="small"
          autoLayout
          resizableColumns
          columnResizeMode="expand"
          // scrollable
          scrollHeight="18rem"
          showGridlines
          responsiveLayout="scroll"
        >
          <Column
            field="User"
            header="User"
            align="center"
            body={User}
          ></Column>
          <Column
            field="channel_number"
            header="Channel Number"
            body={ChannelNumber}
            align="center"
          ></Column>
          {trustzoneSupported !== null && trustzoneSupported && (
            <Column
              field="Security Mode"
              header="Security Mode"
              align="center"
              body={SecurityMode}
            ></Column>
          )}
          <Column
            field="Remove_User"
            header={() => {
              return (
                <React.Fragment>
                  Remove
                  <br />
                  User
                </React.Fragment>
              );
            }}
            align="center"
            body={RemoveUser}
          ></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default UserTable;
