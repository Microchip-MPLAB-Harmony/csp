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
import { component_id } from '../MainView/MainBlock';
import { RowAndVectorInterruptMap } from './Script';
import { GetLabelWithCustomDisplayWithTooltip } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';
import {
  GetSymbolArray,
  GetSymbolValue,
  UpdateSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';

import { Column } from 'primereact/column';
import { DataTable } from 'primereact/datatable';
import { error } from '@mplab_harmony/harmony-plugin-core-service';

const InterruptTable = () => {
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < RowAndVectorInterruptMap.size; i++) {
      dataArr.push({ id: i });
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
    let symbolId = RowAndVectorInterruptMap.get(rowData.id).split('_');
    return <div>{symbolId[0]}</div>;
  };

  const VectorNameAndCaption = (rowData: any) => {
    let vectorName = GetSymbolValue(
      component_id,
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_VECTOR_NAME'
    );
    let caption = GetSymbolValue(
      component_id,
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_CAPTION'
    );
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

  const EnableColumn = (rowData: any) => {
    function EnabledChangeListner(event: { value: any }) {
      // props.parentUpdate();
    }
    let symbolId =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_ENABLE';
    let enableLockId =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_ENABLE_LOCK';
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId, enableLockId]}
          onChange={EnabledChangeListner}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={{ width: '20px', height: '20px' }}
          readOnly={getReadOnlyOnLockedSymbol(component_id, enableLockId)}
          visible={true}
        />
      </div>
    );
  };

  const PriorityColumn = (rowData: any) => {
    function PriorityBoxChanged(event: { value: any }) {
      let nvicId = RowAndVectorInterruptMap.get(rowData.id);
      PriorityChanged(event.value, nvicId);
    }
    let symbolID =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_PRIORITY';
    let priorityLockId =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_PRIORITY_LOCK';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolID}
          symbolListeners={[symbolID, priorityLockId]}
          onChange={PriorityBoxChanged}
          symbolValue={GetSymbolValue(component_id, symbolID)}
          symbolArray={GetSymbolArray(component_id, symbolID)}
          readOnly={getReadOnlyOnLockedSymbol(component_id, priorityLockId)}
          styleObject={{ width: '100px', height: '35px' }}
          visible={true}
        />
      </div>
    );
  };

  const HandlerColumn = (rowData: any) => {
    function HandlerChanged() {
      //
    }
    let symbolId =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_HANDLER';
    let handlerLockId =
      'NVIC_' + RowAndVectorInterruptMap.get(rowData.id) + '_HANDLER_LOCK';
    return (
      <div className="p-d-flex">
        <InputText
          component_id={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId, handlerLockId]}
          styleObject={{ width: '250px' }}
          onChange={HandlerChanged}
          readOnly={getReadOnlyOnLockedSymbol(component_id, handlerLockId)}
          visible={true}
        />
      </div>
    );
  };

  function getReadOnlyOnLockedSymbol(component_id: any, lockSymbolId: any) {
    try {
      let symbolValue = GetSymbolValue(component_id, lockSymbolId);
      symbolValue = convertToBoolean(symbolValue);
      if (symbolValue === null || symbolValue === undefined) {
        return false;
      }
      return symbolValue;
    } catch (err) {
      return false;
    }
  }

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
            <Column
              field="Vector"
              header="Vector"
              body={VectorNameAndCaption}
            ></Column>
            <Column
              field="Enable"
              header="Enable"
              body={EnableColumn}
              style={{ width: '100px' }}
            ></Column>
            <Column
              field="Priority (0 = Highest)"
              header="Priority (0 = Highest)"
              body={PriorityColumn}
              style={{ width: '150px' }}
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

export function PriorityChanged(symbolValue: any, nvicId: any) {
  try {
    let szCheckString = nvicId.split('_')[0] + '_';
    for (let i = 0; i < RowAndVectorInterruptMap.size; i++) {
      let value = RowAndVectorInterruptMap.get(i);
      if (value.startsWith(szCheckString)) {
        globalSymbolSStateData
          .get('NVIC_' + value + '_PRIORITY')
          .changeValue(symbolValue);
        UpdateSymbolValue(
          component_id,
          'NVIC_' + value + '_PRIORITY',
          symbolValue
        );
      }
    }
  } catch (err) {
    error('PriorityChange Error : ' + err);
  }
}
