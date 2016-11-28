import rhinoscriptsyntax as rs

__commandname__ = "RingFlat"
def RunCommand( is_interactive ):
    ringSize = rs.GetReal("Ring size", 8.5, 0, 16)
    start_point = rs.GetPoint("Location")
    plane = rs.ViewCPlane()
    start_plane_point = rs.XformWorldToCPlane(start_point, plane)
    circumference = 36.5356 + 2.5534 * ringSize
    end_plane_point = (start_plane_point[0] + circumference, start_plane_point[1], start_plane_point[2])
    end_point = rs.XformCPlaneToWorld(end_plane_point, plane)
    objId = rs.AddLine(start_point, end_point)
    rs.SelectObject(objId)
