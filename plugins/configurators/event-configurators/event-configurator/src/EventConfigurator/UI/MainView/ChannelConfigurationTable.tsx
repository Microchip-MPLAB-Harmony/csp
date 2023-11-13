import React, { useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
// import { DisplayLabel } from "Common/UIComponents/Label";
import { DisplayLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';

// import DropDown from "Common/UIComponents/DropDown";
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import { component_id } from './MainBlock';
// import {
//   GetSymbolValue,
//   GetSymbolArray,
//   GetSymbolReadOnlyStatus,
//   IsTrustZoneSupported,
// } from "Common/SymbolAccess";

import {
  GetSymbolValue,
  GetSymbolArray,
  GetSymbolReadOnlyStatus,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import { IsTrustZoneSupported } from '@mplab_harmony/harmony-plugin-core-service/build/project-service/ProjectService';

import { PrimeIcons } from 'primereact/api';
import ChannelConfigStatusComp from '../Components/ChannelConfigStatusComp';
// import { convertToBoolean } from "Common/Utils";
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
// import { ChangeClassNameState } from "Common/UIComponents/StateChangeUtils";
import { ChangeClassNameState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

const ChannelTable = (props: {
  channelList: string[];
  selectedChnl: string;
  channelSelectionChanged: (value: string) => void;
  onRemoveChannel: (value: string) => void;
}) => {
  const [dummyState, setDummyState] = useState<boolean>(false);

  let trustzoneSupported = convertToBoolean(IsTrustZoneSupported());

  function GetTrustZoneClassName(value: any) {
    if (value === 'SECURE') {
      return 'secure';
    }
    return 'nonsecure';
  }

  const ChannelNumber = (rowData: any) => {
    let chnlNum: string = rowData.replace(/^\D+/g, '');
    let chnlName = 'Channel ' + chnlNum;
    return <DisplayLabel labelName={chnlName} />;
  };

  const EventGenerator = (rowData: any) => {
    function ConfigurationChanged(event: { value: any }) {
      // do nothing
    }

    const chnlNum: number = rowData.replace(/^\D+/g, '');
    const symbol = 'EVSYS_CHANNEL_' + chnlNum + '_GENERATOR';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbol}
          symbolListeners={[symbol]}
          onChange={ConfigurationChanged}
          symbolValue={GetSymbolValue(component_id, symbol)}
          symbolArray={GetSymbolArray(component_id, symbol)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbol)}
          styleObject={{}}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  const SecurityMode = (rowData: any) => {
    function ConfigurationChanged(event: { value: any }) {
      ChangeClassNameState(
        'EVSYS_NONSEC_' + chnlNum,
        GetTrustZoneClassName(event.value)
      );
    }

    const chnlNum: Number = rowData.replace(/^\D+/g, '');
    const symbol = 'EVSYS_NONSEC_' + chnlNum;

    const symValue = GetSymbolValue(component_id, symbol);
    return (
      <div className="p-d-flex secure-combo">
        <DropDown
          componentId={component_id}
          symbolId={symbol}
          symbolListeners={[symbol]}
          onChange={ConfigurationChanged}
          symbolValue={symValue}
          symbolArray={GetSymbolArray(component_id, symbol)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbol)}
          styleObject={{}}
          visible={true}
          className={GetTrustZoneClassName(symValue)}
        />
      </div>
    );
  };

  const EventStatus = (rowData: any) => {
    const chnlNum: Number = rowData.replace(/^\D+/g, '');
    const symId: string = 'EVSYS_CHANNEL_' + chnlNum + '_GENERATOR_ACTIVE';

    return (
      <ChannelConfigStatusComp
        componentId={component_id}
        symbolId={symId}
        symbolListeners={[symId]}
        readOnly={GetSymbolReadOnlyStatus(component_id, symId)}
        visible={true}
      />
    );
  };

  const UserReady = (rowData: any) => {
    const chnlNum: Number = rowData.replace(/^\D+/g, '');
    const symId: string = 'EVSYS_CHANNEL_' + chnlNum + '_USER_READY';

    return (
      <ChannelConfigStatusComp
        componentId={component_id}
        symbolId={symId}
        symbolListeners={[symId]}
        readOnly={GetSymbolReadOnlyStatus(component_id, symId)}
        visible={true}
      />
    );
  };

  const RemoveChannel = (rowData: any) => {
    return (
      <div
        className={PrimeIcons.TRASH}
        onClick={(e) => {
          props.onRemoveChannel(rowData);
          setDummyState(() => !dummyState);
        }}
      ></div>
    );
  };

  const selectionChanged = (e: any) => {
    props.channelSelectionChanged(e.value);
  };

  return (
    <div key={props.channelList.length}>
      <div className="card">
        <DataTable
          value={props.channelList}
          autoLayout
          stripedRows
          showGridlines
          size="small"
          resizableColumns
          // scrollable
          scrollHeight="18rem"
          // responsiveLayout="scroll"
          columnResizeMode="expand"
          selectionMode="single"
          selection={props.selectedChnl}
          onSelectionChange={selectionChanged}
        >
          <Column
            field="channel_number"
            header="Channel Number"
            align="center"
            body={ChannelNumber}
          ></Column>
          <Column
            field="Event_Generator"
            header="Event Generator"
            align="center"
            body={EventGenerator}
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
            field="Event_Status"
            header={() => {
              return (
                <React.Fragment>
                  Event
                  <br />
                  Status
                </React.Fragment>
              );
            }}
            align="center"
            resizeable
            body={EventStatus}
          ></Column>
          <Column
            field="User_Ready"
            header={() => {
              return (
                <React.Fragment>
                  User
                  <br />
                  Ready
                </React.Fragment>
              );
            }}
            align="center"
            body={UserReady}
          ></Column>
          <Column
            field="Remove_Channel"
            header={() => {
              return (
                <React.Fragment>
                  Remove
                  <br />
                  Channel
                </React.Fragment>
              );
            }}
            align="center"
            body={RemoveChannel}
          ></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default ChannelTable;
