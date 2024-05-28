import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import { GetIconButton } from './NodeType';
import MultipleUIComponentsWithLabel from './MultipleUIComponentsWithLabel';
import { useState } from 'react';

const SettingsDialog = (props: {
  tooltip: string;
  className: string;
  componentId: string;
  symbolArray: string[];
  dialogWidth: string;
  dialogHeight: string;
}) => {
  const [settingDialogStatus, setSettingDialogStatus] = useState(false);

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
        tooltip={props.tooltip}
        icon='pi pi-cog'
        className={props.className}
        onClick={() => setSettingDialogStatus(true)}
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
