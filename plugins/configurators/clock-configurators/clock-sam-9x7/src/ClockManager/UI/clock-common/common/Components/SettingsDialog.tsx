import { AddMultipleUIComponentsWithLabel } from '@mplab_harmony/harmony-plugin-ui';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import { GetIconButton } from './NodeType';

const SettingsDialog = (props: {
  tooltip: string;
  className: string;
  componentId: string;
  symbolArray: string[];
  onChange?: (onChangeData: Map<String, any>) => void;
  dialogWidth: string;
  dialogHeight: string;
  visibleStatus: boolean;
  dialogStatus: (dialogVisibleStatus: boolean) => void;
}) => {
  function onDialogClick() {
    props.dialogStatus(true);
  }
  function onHide() {
    props.dialogStatus(false);
  }

  function onSymbolChangeData(onChangeData: Map<String, any>) {
    props.onChange?.(onChangeData);
  }
  const footer = (
    <div>
      <Button
        label='Close'
        icon='pi pi-check'
        onClick={onHide}
      />
    </div>
  );

  return (
    <div>
      <GetIconButton
        tooltip={props.tooltip}
        icon='pi pi-cog'
        className={props.className}
        onClick={onDialogClick}
      />
      <Dialog
        header={props.tooltip}
        footer={footer}
        visible={props.visibleStatus}
        closeOnEscape
        dismissableMask
        resizable
        position={'center'}
        modal
        style={{ width: props.dialogWidth, height: props.dialogHeight }}
        onHide={onHide}>
        <div>
          <AddMultipleUIComponentsWithLabel
            componentId={props.componentId}
            onChange={onSymbolChangeData}
            symbolsArray={props.symbolArray}
          />
        </div>
      </Dialog>
    </div>
  );
};
export default SettingsDialog;
