import { Column } from 'primereact/column';
import { DataTable } from 'primereact/datatable';

import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';
import { component_id } from '../MainView/MainBlock';
import {
  GetSymbolValue,
  GetSymbolArray,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import styles from './MPURegionSettings.module.css';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import React, { useContext } from 'react';
import MPUContext from 'MPUConfigurator/store/MPUContext';

interface MPUProps {
  regions: number[];
}

const MPURegionSettings = (props: MPUProps) => {
  const MPUctx = useContext(MPUContext);

  const RegionId = (rowData: number) => {
    return rowData;
  };

  const convertDecimalToHex = (decimalNumber: any) => {
    decimalNumber = parseInt(decimalNumber);
    if (Number.isNaN(decimalNumber)) {
      return '0x0';
    }
    let hexString = '0x' + decimalNumber.toString(16);
    return hexString;
  };

  const convertHexToDecimal = (hex: any) => {
    let hexString = String(hex);
    if (hexString === '0x') {
      hexString = '0x0';
    }
    let hexNumber = parseInt(hexString, 16);
    return hexNumber;
  };

  const RegionEnable = (rowData: number) => {
    return (
      <CheckBox
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Enable'}
        symbolListeners={['MPU_Region_' + rowData + '_Enable']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Enable'
        )}
        styleObject={{}}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const MemorySpace = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'MPU_Region_Name' + rowData}
        symbolListeners={['MPU_Region_Name' + rowData]}
        symbolValue={GetSymbolValue(component_id, 'MPU_Region_Name' + rowData)}
        symbolArray={GetSymbolArray(component_id, 'MPU_Region_Name0_Options')}
        styleObject={null}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const RegionName = (rowData: number) => {
    return (
      <InputText
        component_id={component_id}
        symbolId={'MPU_Region_Name' + rowData}
        symbolListeners={['MPU_Region_Name' + rowData]}
        styleObject={{ maxWidth: '9rem' }}
        className={null}
        onChange={() => {}}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
      />
    );
  };

  const StartAddress = (rowData: number) => {
    return (
      <InputText
        component_id={component_id}
        symbolId={'MPU_Region_' + rowData + '_Address'}
        symbolListeners={['MPU_Region_' + rowData + '_Address']}
        styleObject={{ maxWidth: '8rem' }}
        className={null}
        onChange={() => {}}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        formatInput={convertDecimalToHex}
        formatOutput={convertHexToDecimal}
      />
    );
  };

  const RegionSize = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Size'}
        symbolListeners={['MPU_Region_' + rowData + '_Size']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Size'
        )}
        symbolArray={GetSymbolArray(
          component_id,
          'MPU_Region_' + rowData + '_Size'
        )}
        styleObject={null}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const MemoryType = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Type'}
        symbolListeners={['MPU_Region_' + rowData + '_Type']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Type'
        )}
        symbolArray={GetSymbolArray(
          component_id,
          'MPU_Region_' + rowData + '_Type'
        )}
        styleObject={null}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };
  const DataAccess = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Access'}
        symbolListeners={['MPU_Region_' + rowData + '_Access']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Access'
        )}
        symbolArray={GetSymbolArray(
          component_id,
          'MPU_Region_' + rowData + '_Access'
        )}
        styleObject={null}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const InstructionFetch = (rowData: number) => {
    return (
      <CheckBox
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Execute'}
        symbolListeners={['MPU_Region_' + rowData + '_Execute']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Execute'
        )}
        styleObject={{}}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const Shareable = (rowData: number) => {
    return (
      <CheckBox
        componentId={component_id}
        symbolId={'MPU_Region_' + rowData + '_Share'}
        symbolListeners={['MPU_Region_' + rowData + '_Share']}
        symbolValue={GetSymbolValue(
          component_id,
          'MPU_Region_' + rowData + '_Share'
        )}
        styleObject={{}}
        className={null}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  return (
    <div className={styles.mpu}>
      <DataTable
        value={props.regions}
        stripedRows
        size="small"
        autoLayout
        resizableColumns
        columnResizeMode="expand"
        // scrollable
        scrollHeight="60rem"
        showGridlines
        responsiveLayout="scroll"
      >
        <Column
          field="Region"
          header="Region"
          align="center"
          body={RegionId}
        ></Column>
        <Column
          field="RegionEnable"
          header="Enable"
          align="center"
          body={RegionEnable}
        ></Column>
        <Column
          field="MemorySpace"
          header={
            <React.Fragment>
              Memory
              <br />
              Space
            </React.Fragment>
          }
          align="center"
          body={MemorySpace}
        ></Column>
        <Column
          field="RegionName"
          header={
            <React.Fragment>
              Region
              <br />
              Name
            </React.Fragment>
          }
          align="center"
          body={RegionName}
        ></Column>
        <Column
          field="StartAddress"
          header={
            <React.Fragment>
              Start
              <br />
              Address(Hex)
            </React.Fragment>
          }
          align="center"
          body={StartAddress}
        ></Column>
        <Column
          field="RegionSize"
          header={
            <React.Fragment>
              Region
              <br />
              Size
            </React.Fragment>
          }
          align="center"
          body={RegionSize}
        ></Column>
        <Column
          field="MemoryType"
          header="Memory Type"
          align="center"
          body={MemoryType}
        ></Column>
        <Column
          field="DataAccess"
          header="Data Access"
          align="center"
          body={DataAccess}
        ></Column>
        <Column
          field="InstructionFetch"
          header={
            <React.Fragment>
              Instruction
              <br />
              Fetch
            </React.Fragment>
          }
          align="center"
          body={InstructionFetch}
        ></Column>
        <Column
          field="Shareable"
          header="Shareable"
          // style={{ horizontalAlign: 'center', borderColor: 'red' }}
          align="center"
          body={Shareable}
        ></Column>
      </DataTable>
    </div>
  );
};

export default MPURegionSettings;
