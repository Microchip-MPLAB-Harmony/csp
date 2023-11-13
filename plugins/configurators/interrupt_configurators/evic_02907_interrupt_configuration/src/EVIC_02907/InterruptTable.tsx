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

import '../Styles/index.css';
import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import { GetLabelWithCustomDisplayWithTooltip } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';

let inputTextStyle: any = new Map<string, string>();
inputTextStyle.set('width', '250px');

let ROWID_NAME_INTERRUPTID_OBJECT_MAP: any = {};

const InterruptTable = () => {
  let customLabelsArray = createCustomLengthArray();

  // let trustzoneSupported = convertToBoolean(IsTrustZoneSupported());

  function createCustomLengthArray() {
    let dataArr = [];
    let idSymbolArray = GetSymbolArray(
      component_id,
      'EVIC_GUI_COLUMN_VECTOR_ID'
    );
    for (let i = 0; i < idSymbolArray.length; i++) {
      dataArr.push({ id: i });
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[i] = {
        id: idSymbolArray[i],
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

  const VectorNumber = (rowData: any) => {
    let symbolId = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    return <div>{symbolId}</div>;
  };

  const NameColumn = (rowData: any) => {
    let id = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    let vectorName = GetSymbolValue(component_id, 'EVIC_' + id + '_NAME');
    let caption = GetSymbolValue(component_id, 'EVIC_' + id + '_CAPTION_UI');
    let tooltip = caption;
    caption = String(caption);
    if (caption.length > 50) {
      caption = caption.substring(0, 50) + '...';
    }

    return (
      <div>
        {GetLabel(
          vectorName + '  (' + caption + ') ',
          'CAPTION : (' + tooltip + ')'
        )}
      </div>
    );
  };

  function getReadOnly(component_id: any, symbolId: any) {
    try {
      let symbolValue = GetSymbolValue(component_id, symbolId);
      symbolValue = convertToBoolean(symbolValue);
      if (symbolValue === null || symbolValue === undefined) {
        return false;
      }
      return symbolValue;
    } catch (err) {
      return false;
    }
  }

  const UseColumn = (rowData: any) => {
    function UseColumnChangeListener(event: { value: any }) {
      // props.parentUpdate();
    }
    let id = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    let symbolId = 'EVIC_' + id + '_ENABLE';
    let enableLockId = 'EVIC_' + id + '_ENABLE_LOCK';
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId, enableLockId]}
          onChange={UseColumnChangeListener}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={{ width: '20px', height: '20px' }}
          className={null}
          readOnly={getReadOnly(component_id, enableLockId)}
          visible={true}
        />
      </div>
    );
  };

  const PriorityColumn = (rowData: any) => {
    function PriorityColumnChanged(event: { value: any }) {
      // do nothing
    }
    let id = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    let symbolId = 'EVIC_' + id + '_PRIORITY';
    let priorityLockId = 'EVIC_' + id + '_PRIORITY_LOCK';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId, priorityLockId]}
          onChange={PriorityColumnChanged}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={getReadOnly(component_id, priorityLockId)}
          styleObject={{ width: '150px', height: '35px' }}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  const SubPriorityColumn = (rowData: any) => {
    function SubPriorityColumnChangeListener(event: { value: any }) {
      // do nothing
    }
    let id = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    let symbolId = 'EVIC_' + id + '_SUBPRIORITY';
    let subPriorityLockId = 'EVIC_' + id + '_SUBPRIORITY_LOCK';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId, subPriorityLockId]}
          onChange={SubPriorityColumnChangeListener}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={getReadOnly(component_id, subPriorityLockId)}
          styleObject={{ width: '150px', height: '35px' }}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  const HandlerColumn = (rowData: any) => {
    function HandlerChanged() {
      //
    }
    let id = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id'];
    let symbolId = 'EVIC_' + id + '_HANDLER';
    let handlerLockId = 'EVIC_' + id + '_HANDLER_LOCK';
    return (
      <InputText
        component_id={component_id}
        symbolId={symbolId}
        symbolListeners={[symbolId, handlerLockId]}
        styleObject={Object.fromEntries(inputTextStyle)}
        className={null}
        onChange={HandlerChanged}
        readOnly={getReadOnly(component_id, handlerLockId)}
        visible={true}
      />
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
              field="Vector Number"
              header="Vector Number"
              body={VectorNumber}
            ></Column>
            <Column field="Name" header="Name" body={NameColumn}></Column>
            <Column field="Use" header="Use" body={UseColumn}></Column>
            <Column
              field="Priority ( 1 = Lowest )"
              header="Priority ( 1 = Lowest )"
              body={PriorityColumn}
            ></Column>
            <Column
              field="SubPriority"
              header="SubPriority"
              body={SubPriorityColumn}
            ></Column>
            <Column
              field="HandlerName"
              header="HandlerName"
              body={HandlerColumn}
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default InterruptTable;
