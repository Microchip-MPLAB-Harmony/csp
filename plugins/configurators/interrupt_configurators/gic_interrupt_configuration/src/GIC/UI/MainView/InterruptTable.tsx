/*
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 */
import { component_id } from './MainBlock';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';

import './../../../Styles/SecureCombo.css';
import './../../../Styles/index.css';
import {
  GetSymbolArray,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolReadOnlyStatus,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetLabelWithCustomDisplayWithTooltip } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import { GetMinFractionValueBasedSymbolType } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';
import { ChangeClassNameState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import InputNumber from '@mplab_harmony/harmony-plugin-ui/build/components/InputNumber';

let inputTextStyle: any = new Map<string, string>();
inputTextStyle.set('width', '250px');

let secureClassName = 'secure';
let nonSecureClassName = 'nonsecure';
let ROWID_NAME_INTERRUPTID_OBJECT_MAP: any = {};

const InterruptTable = () => {
  let customLabelsArray = createCustomLengthArray();

  // let trustzoneSupported = convertToBoolean(IsTrustZoneSupported());

  function createCustomLengthArray() {
    let dataArr = [];
    let idSymbolArray = GetSymbolArray(component_id, 'GIC_COLUMN_ID');
    let nameSymbolArray: any = GetSymbolArray(component_id, 'GIC_COLUMN_NAME');
    for (let i = 0; i < nameSymbolArray.length; i++) {
      dataArr.push({ id: i });
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[i] = {
        id: idSymbolArray[i],
        name: nameSymbolArray[i],
      };
    }
    return dataArr;
  }

  function GetLabel(displayValue: string, tooltip: any) {
    return (
      <div>
        <GetLabelWithCustomDisplayWithTooltip
          labelId={''}
          labelDisplayText={displayValue}
          labelStyle={null}
          labelTooltip={tooltip}
        />
      </div>
    );
  }

  const IdNumber = (rowData: any) => {
    let symbolId = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    return <div>{symbolId}</div>;
  };

  const TypeColumn = (rowData: any) => {
    let symbolId = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    if (symbolId > 31) {
      return <div> SPI </div>;
    }
    return <div> PPI </div>;
  };

  const NameColumn = (rowData: any) => {
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    return <div>{GetLabel(name, name)}</div>;
  };

  const EnableColumn = (rowData: any) => {
    function EnabledChangeListner(event: { value: any }) {
      // props.parentUpdate();
    }
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    let symbolId = name + '_INTERRUPT_ENABLE';
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId]}
          onChange={EnabledChangeListner}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={{ width: '20px', height: '20px' }}
          className={null}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={true}
        />
      </div>
    );
  };

  const ConfigurationColumn = (rowData: any) => {
    function ConfigurationChanged(event: { value: any }) {
      // do nothing
    }
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    let symbolId = name + '_INTERRUPT_CONFIG';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId]}
          onChange={ConfigurationChanged}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={{ width: '150px', height: '35px' }}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  const PriorityColumn = (rowData: any) => {
    function PriorityBoxChanged(event: { value: any }) {
      // do nothing
    }
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    let symbolId = name + '_INTERRUPT_PRIORITY';
    return (
      <div className="p-fluid">
        <InputNumber
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId]}
          onChange={PriorityBoxChanged}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={{ width: '180px', height: '35px' }}
          visible={true}
          className={null}
          minFractionValue={GetMinFractionValueBasedSymbolType(
            component_id,
            symbolId
          )}
          minValue={GetSymbolMinValue(component_id, symbolId)}
          maxValue={GetSymbolMaxValue(symbolId, symbolId)}
        />
      </div>
    );
  };

  const HandlerColumn = (rowData: any) => {
    function HandlerChanged() {
      //
    }
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    let symbolId = name + '_INTERRUPT_HANDLER';
    return (
      <InputText
        component_id={component_id}
        symbolId={symbolId}
        symbolListeners={[symbolId]}
        styleObject={Object.fromEntries(inputTextStyle)}
        className={null}
        onChange={HandlerChanged}
        readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
        visible={true}
      />
    );
  };

  const Security = (rowData: any) => {
    function SecurityChanged(event: { value: any }) {
      ChangeClassNameState(
        ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'] +
          '_INTERRUPT_SECURITY',
        GetTrustZoneClassName(event.value)
      );
    }

    let symbolId =
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'] +
      '_INTERRUPT_SECURITY';
    let symbolValue = GetSymbolValue(component_id, symbolId);

    return (
      <div className="p-d-flex secure-combo">
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId]}
          onChange={SecurityChanged}
          symbolValue={symbolValue}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={{ height: '35px', width: '200px' }}
          visible={true}
          className={GetTrustZoneClassName(symbolValue)}
        />
      </div>
    );
  };

  return (
    <div>
      <div className="p-d-flex">
        <div className="card">
          <DataTable
            value={customLabelsArray}
            stripedRows
            size="small"
            resizableColumns
            scrollHeight="flex"
            showGridlines
            responsiveLayout="scroll"
            columnResizeMode="expand"
          >
            <Column
              field="Id"
              header="Id"
              body={IdNumber}
              style={{ width: '130px' }}
            ></Column>
            <Column
              field="Type"
              header="Type"
              body={TypeColumn}
              style={{ width: '130px' }}
            ></Column>
            <Column
              field="Name"
              header="Name"
              body={NameColumn}
              style={{ width: '200px' }}
            ></Column>
            <Column
              field="Enable"
              header="Enable"
              body={EnableColumn}
              style={{ width: '100px' }}
            ></Column>
            <Column
              field="Handler"
              header="Handler"
              body={HandlerColumn}
              style={{ width: '230px' }}
            ></Column>
            <Column
              field="Configuration"
              header="Configuration"
              body={ConfigurationColumn}
            ></Column>
            <Column
              field="Priority"
              header="Priority"
              body={PriorityColumn}
            ></Column>
            <Column
              field="Security Mode"
              header="Security Mode"
              body={Security}
            ></Column>
            {/* {trustzoneSupported !== null && trustzoneSupported && (
              <Column
                field="Security Mode"
                header="Security Mode"
                body={Security}
              ></Column>
            )} */}
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default InterruptTable;

export function GetTrustZoneClassName(value: any) {
  if (value === 'SECURE') {
    return secureClassName;
  }
  return nonSecureClassName;
}
