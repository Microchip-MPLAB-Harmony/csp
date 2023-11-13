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

import './../../../Styles/index.css';
import useForceUpdate from 'use-force-update';
import {
  GetSymbolArray,
  GetSymbolReadOnlyStatus,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';
import { StateLabel, getIndex } from '@mplab_harmony/harmony-plugin-ui';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

let inputTextStyle: any = new Map<string, string>();
inputTextStyle.set('width', '250px');

let ROWID_NAME_INTERRUPTID_OBJECT_MAP: any = {};
let sharedIdAndParentVectorName: any = new Map<string, string>();

const InterruptTable = () => {
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    let idSymbolArray: any = GetSymbolArray(component_id, 'AIC_GUI_VECTOR_IDS');
    let nameSymbolArray: any = GetSymbolArray(
      component_id,
      'AIC_GUI_VECTOR_NAMES'
    );
    let vectorNameAndDescriptionSymbolArray: any = GetSymbolArray(
      component_id,
      'AIC_GUI_COLUMN_VECTOR_NAME_AND_DESCRIPTION'
    );
    for (let i = 0; i < idSymbolArray.length; i++) {
      if (!IsParentVector(i, idSymbolArray[i], idSymbolArray)) {
        dataArr.push({ id: i });
        ROWID_NAME_INTERRUPTID_OBJECT_MAP[i] = {
          id: idSymbolArray[i],
          name: nameSymbolArray[i],
          vectorNameAndDescription: vectorNameAndDescriptionSymbolArray[i],
          isSharedVector: checkForSharedVectors(
            idSymbolArray[i],
            idSymbolArray,
            nameSymbolArray
          ),
        };
      }
    }
    return dataArr;
  }

  const update = useForceUpdate();

  function IsParentVector(
    currentIndex: any,
    currentVector: string,
    array: any
  ) {
    if (currentVector.endsWith('_0') && currentIndex !== array.length - 1) {
      let nextVector = array[currentIndex + 1];
      if (!nextVector.endsWith('_0')) {
        return true;
      }
    }
    return false;
  }

  function checkForSharedVectors(
    vectorId: string,
    idArray: any,
    nameSymbolArray: any
  ) {
    if (!vectorId.endsWith('_0')) {
      let parentId = vectorId.split('_')[0] + '_0';
      let name = nameSymbolArray[getIndex(parentId, idArray)];
      sharedIdAndParentVectorName.set(vectorId, name);
      return true;
    }
    return false;
  }

  const VectorColumn = (rowData: any) => {
    return (
      <div>
        {
          <StateLabel
            labelDisplayText={
              ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id][
                'vectorNameAndDescription'
              ]
            }
          ></StateLabel>
        }
      </div>
    );
  };

  const EnableColumn = (rowData: any) => {
    function EnabledChangeListner(onChangeData: any) {
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

  const HandlerColumn = (rowData: any) => {
    function HandlerChanged(onChangeData: any) {
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

  const MapType = (rowData: any) => {
    let sharedIdStatus =
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['isSharedVector'];
    let name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    let displayText;
    if (sharedIdStatus) {
      displayText = '';
    } else {
      displayText = GetSymbolValue(component_id, name + '_INTERRUPT_MAP_TYPE');
    }
    return (
      <div>{<StateLabel labelDisplayText={displayText}></StateLabel>}</div>
    );
  };

  const SourceType = (rowData: any) => {
    let sharedIdStatus =
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['isSharedVector'];

    function ConfigurationChanged(onChangeData: any) {
      if (
        sharedIdAndParentVectorName.has(
          ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id']
        )
      ) {
        update();
      }
    }

    let name;
    if (sharedIdStatus) {
      name = sharedIdAndParentVectorName.get(
        ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id']
      );
    } else {
      name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    }
    let symbolId = name + '_INTERRUPT_SRC_TYPE';
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
          styleObject={{ height: '35px' }}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  const PriorityColumn = (rowData: any) => {
    let sharedIdStatus =
      ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['isSharedVector'];

    function PriorityBoxChanged(onChangeData: any) {
      if (
        sharedIdAndParentVectorName.has(
          ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id']
        )
      ) {
        update();
      }
    }

    let name;
    if (sharedIdStatus) {
      name = sharedIdAndParentVectorName.get(
        ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['id']
      );
    } else {
      name = ROWID_NAME_INTERRUPTID_OBJECT_MAP[rowData.id]['name'];
    }
    let symbolId = name + '_INTERRUPT_PRIORITY';
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          symbolListeners={[symbolId]}
          onChange={PriorityBoxChanged}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={{ width: '250px', height: '35px' }}
          visible={true}
          className={null}
        />
      </div>
    );
  };

  return (
    <div>
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
            field="Vector"
            header="Vector"
            body={VectorColumn}
            style={{ width: '200px' }}
          ></Column>
          <Column
            field="Enable"
            header="Enable"
            body={EnableColumn}
            style={{ width: '100px' }}
          ></Column>
          <Column
            field="Handler Name"
            header="Handler Name"
            body={HandlerColumn}
            style={{ width: '130px' }}
          ></Column>
          <Column
            field="Map Type"
            header="Map Type"
            body={MapType}
            style={{ width: '150px' }}
          ></Column>
          <Column
            field="Source Type"
            header="Source Type"
            body={SourceType}
          ></Column>
          <Column
            field="Priority"
            header="Priority"
            body={PriorityColumn}
          ></Column>
        </DataTable>
      </div>
    </div>
  );
};
export default InterruptTable;
