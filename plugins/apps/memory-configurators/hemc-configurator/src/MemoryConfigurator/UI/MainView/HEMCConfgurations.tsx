import { Column } from 'primereact/column';
import { DataTable } from 'primereact/datatable';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputText from '@mplab_harmony/harmony-plugin-ui/build/components/InputText';

import { component_id } from './MainBlock';
import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import DisplayConflict from '../components/DisplayConflict';
import styles from './HEMC.module.css';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import DisplayEndAddress from '../components/DisplayEndAddress';
import ECCStatus from '../components/ECCStatus';

const HEMCConfigurations = () => {
  const chipSelectCount = () => {
    const count = GetSymbolValue(component_id, 'HSMC_CHIP_SELECT_COUNT');
    const arr = [];
    for (let i = 0; i < count; i++) {
      arr.push(i);
    }
    return arr;
  };

  const chipSelect = chipSelectCount();

  const ConflictStatus = (rowData: number) => {
    return <DisplayConflict index={rowData} />;
  };

  const ChipSelect = (rowData: number) => {
    return 'Chip Select ' + rowData;
  };

  const StartAddress = (rowData: number) => {
    return (
      <InputText
        component_id={component_id}
        symbolId={'CS_' + rowData + '_START_ADDRESS'}
        symbolListeners={['CS_' + rowData + '_START_ADDRESS']}
        styleObject={{ maxWidth: '8rem' }}
        className={null}
        readOnly={false}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const EndAddress = (rowData: number) => {
    return <DisplayEndAddress index={rowData} />;
  };

  const BankSize = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'CS_' + rowData + '_MEMORY_BANK_SIZE'}
        symbolListeners={['CS_' + rowData + '_MEMORY_BANK_SIZE']}
        symbolValue={GetSymbolValue(
          component_id,
          'CS_' + rowData + '_MEMORY_BANK_SIZE'
        )}
        symbolArray={GetSymbolArray(
          component_id,
          'CS_' + rowData + '_MEMORY_BANK_SIZE'
        )}
        styleObject={null}
        className={null}
        readOnly={false}
        visible={true}
        onChange={(event) => {
          globalSymbolSStateData
            .get('CS_' + rowData + '_COMMENT')
            .setVisibilityStatus(event.value !== 'NOT_USED');
        }}
      />
    );
  };

  const MemoryType = (rowData: number) => {
    return (
      <DropDown
        componentId={component_id}
        symbolId={'CS_' + rowData + '_MEMORY_TYPE'}
        symbolListeners={[]}
        symbolValue={GetSymbolValue(
          component_id,
          'CS_' + rowData + '_MEMORY_TYPE'
        )}
        symbolArray={GetSymbolArray(
          component_id,
          'CS_' + rowData + '_MEMORY_TYPE'
        )}
        styleObject={null}
        className={null}
        readOnly={false}
        visible={true}
        onChange={() => {}}
      />
    );
  };

  const EnableECC = (rowData: number) => {
    return <ECCStatus index={rowData} />;
  };

  return (
    <div className={styles.hemc}>
      <DataTable
        value={chipSelect}
        stripedRows
        size="small"
        autoLayout
        resizableColumns
        columnResizeMode="expand"
        // scrollable
        scrollHeight="25rem"
        showGridlines
        responsiveLayout="scroll"
      >
        <Column
          field="conflictStatus"
          header="Status"
          align="center"
          body={ConflictStatus}
        ></Column>
        <Column
          field="chipSelect"
          header="Chip Select"
          align="center"
          body={ChipSelect}
        ></Column>
        <Column
          field="startAddress"
          header="Start Address"
          align="center"
          body={StartAddress}
        ></Column>
        <Column
          field="endAddress"
          header="End Address"
          align="center"
          body={EndAddress}
        ></Column>
        <Column
          field="bankSize"
          header="Bank Size"
          align="center"
          body={BankSize}
        ></Column>
        <Column
          field="memoryType"
          header="Memory Type"
          align="center"
          body={MemoryType}
        ></Column>
        <Column
          field="enableEcc"
          header="ECC Status"
          align="center"
          body={EnableECC}
        ></Column>
      </DataTable>
    </div>
  );
};

export default HEMCConfigurations;
