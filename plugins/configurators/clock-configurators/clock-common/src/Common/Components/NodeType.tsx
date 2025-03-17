import { Button, ButtonProps } from 'primereact/button';

interface CustomIconProps {
  tooltip: string;
  className: string;
  icon: string;
  onClick: () => void;
}
export const GetIconButton = (props: CustomIconProps & ButtonProps) => {
  const newClass =
    'p-button-rounded p-button-text p-button-plain p-button-lg p-mr-1 ' + props.className;
  return (
    <div>
      <Button
        tooltipOptions={{ position: 'right' }}
        style={{ color: 'black' }}
        aria-label='Filter'
        {...props}
        className={newClass}
      />
    </div>
  );
};
interface CustomProps {
  label: string;
  className: string;
  tooltip: string;
  onClick: (arg0: any) => void;
}
export function GetButton(props: CustomProps & ButtonProps) {
  try {
    return (
      <Button
        aria-label='Filter'
        tooltipOptions={{ position: 'right' }}
        {...props}
      />
    );
  } catch (err) {
    return <div></div>;
  }
}
