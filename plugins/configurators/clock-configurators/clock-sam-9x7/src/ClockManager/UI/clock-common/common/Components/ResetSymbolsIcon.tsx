import { Toast } from 'primereact/toast';
import { useRef } from 'react';
import { GetIconButton } from './NodeType';
import { clearAllSymbols } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import { confirmDialog } from 'primereact/confirmdialog';

const ResetSymbolsIcon = (props: {
  tooltip: string;
  className: string;
  componentId: string;
  resetSymbolsArray: string[];
}) => {
  const toastRef = useRef<any>();

  function showToast() {
    toastRef.current.show({
      severity: 'success',
      summary: 'Reset to Default Action Completed!',
      life: 4000
    });
    return null;
  }

  function callConfirmDialog(componentID: String, symbolsArray: string[]) {
    function acceptAction() {
      clearAllSymbols(componentID, symbolsArray);
      showToast();
    }
    confirmDialog({
      message: 'Are you sure you want to proceed?',
      header: 'Confirmation',
      icon: 'pi pi-exclamation-triangle',
      accept: () => acceptAction(),
      reject: () => null
    });
  }

  function ResetClick() {
    callConfirmDialog(props.componentId, props.resetSymbolsArray);
  }

  return (
    <div>
      <Toast
        ref={toastRef}
        position='bottom-right'></Toast>
      <GetIconButton
        tooltip={props.tooltip}
        className={props.className}
        onClick={ResetClick}
        icon={'pi pi-refresh'}
      />
    </div>
  );
};
export default ResetSymbolsIcon;
