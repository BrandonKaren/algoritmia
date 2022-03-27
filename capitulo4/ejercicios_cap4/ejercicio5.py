color = '#AF549B'

match color:
    case '#FF0000':
        print('🔴')
        
    case '#00FF00':
        print('🟢')
        
    case '#0000FF':
        print('🔵')
    case _:
        print('color desconocido')