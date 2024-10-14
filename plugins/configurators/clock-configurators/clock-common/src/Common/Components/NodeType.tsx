import { Button } from 'primereact/button';

export const GetIconButton = (props: {
  tooltip: string;
  icon: string;
  className: string;
  onClick: () => void;
}) => {
  const newClass =
    'p-button-rounded p-button-text p-button-plain p-button-lg p-mr-1 ' + props.className;
  return (
    <div>
      <Button
        tooltip={props.tooltip}
        tooltipOptions={{ position: 'right' }}
        icon={props.icon}
        style={{ color: 'black' }}
        className={newClass}
        aria-label='Filter'
        onClick={props.onClick}
      />
    </div>
  );
};

export function GetButton(props: {
  buttonDisplayText: string;
  className: string;
  toolTip: string;
  buttonClick: (arg0: any) => void;
}) {
  try {
    return (
      <Button
        aria-label='Filter'
        tooltip={props.toolTip}
        onClick={props.buttonClick}
        label={props.buttonDisplayText}
        className={props.className}
      />
    );
  } catch (err) {
    return <div></div>;
  }
}
