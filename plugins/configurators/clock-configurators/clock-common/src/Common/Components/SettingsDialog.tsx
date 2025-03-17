import { Button, ButtonProps } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import { GetIconButton } from './NodeType';
import { useState } from 'react';
import MultipleUIComponentsWithLabel from './MultipleUIComponentsWithLabel';
interface SettingsProps {
  tooltip: string;
  className: string;
  componentId: string;
  symbolArray: string[];
  dialogWidth: string;
  dialogHeight: string;
}
const SettingsDialog = (props: SettingsProps & ButtonProps) => {
  const [settingDialogStatus, setSettingDialogStatus] = useState(false);
  const { componentId, symbolArray, dialogWidth, dialogHeight, ...expectProps } = props;
  const footer = (
    <div>
      <Button
        label='Close'
        icon='pi pi-check'
        onClick={() => setSettingDialogStatus(false)}
      />
    </div>
  );

  return (
    <div>
      <GetIconButton
        {...expectProps}
        onClick={() => setSettingDialogStatus(true)}
        icon='pi pi-cog'
      />

      <Dialog
        header={props.tooltip}
        footer={footer}
        visible={settingDialogStatus}
        closeOnEscape
        dismissableMask
        resizable
        position={'center'}
        modal
        style={{ width: props.dialogWidth, height: props.dialogHeight }}
        onHide={() => setSettingDialogStatus(false)}>
        <div>
          <MultipleUIComponentsWithLabel
            componentId={props.componentId}
            symbolsArray={props.symbolArray}
          />
        </div>
      </Dialog>
    </div>
  );
};
export default SettingsDialog;
